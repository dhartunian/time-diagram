import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

class TimeDiagram:

    def __init__(self, start_hours, end_hours, labels):
        self.item_times = np.array([start_hours, end_hours]).transpose()
        self.item_names = labels

    def hourToAngle(self, hour):
        angle = ((5.0/2.0) - (hour / 6.0)) * np.pi
        while angle > (2*np.pi):
            angle = angle - (2*np.pi)
        return angle

    def hourToNextAngle(self, hour, start_angle):
        end_angle = ((5.0/2.0) - (hour / 6.0)) * np.pi
        while end_angle < start_angle:
            end_angle = end_angle + (2 * np.pi)
        return end_angle

    def drawPair(self, pair, label):
        start_angle = self.hourToAngle(pair[1])
        end_angle = self.hourToNextAngle(pair[0], start_angle)
        new_angles = np.linspace(start_angle, end_angle, 20)
        new_points = np.ones(len(new_angles))
        plt.polar(new_angles, new_points)
        plt.fill_between(new_angles, new_points, facecolor='yellow', alpha=0.5)
        self.drawLabel(new_angles, new_points, label)

    def drawLabel(self, angles, points, label):
        plt.annotate(label,
                     xy = (angles[10], points[10]/2),
                     xytext = (0.1, 0.1),
                     textcoords = 'figure fraction',
                     arrowprops = dict(facecolor='black', shrink=0.05),
                     horizontalalignment = 'right',
                     verticalalignment='top',
                     )

    def drawDiagram(self):
        angles = np.array([])
        points = np.array([])
        for i in range(0, len(self.item_times)):
            pair = self.item_times[i]
            label = self.item_names[i]
            self.drawPair(pair, label)
        
    def formatDiagram(self):
        plt.xticks(np.linspace(np.pi/6,2*np.pi,12), \
                   ('2','1','12','11','10','9','8','7','6','5','4','3'))
        plt.ylim(0,1)
        plt.yticks([0,1],('',''))
        

# tsk = TimeDiagram(np.array([11,3.5, 12]),np.array([11.5,4, 1.5]))
tsk = TimeDiagram(np.array([10]), np.array([9]), "Doctor's Appointment")
tsk.drawDiagram()
tsk.formatDiagram()

