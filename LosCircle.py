from manim import *

class CircleDivision(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=2, color=BLUE, fill_color=BLUE, fill_opacity=0.3)

        # Create a line to divide the circle into two halves
        dividing_line1 = Line(start=circle.point_from_proportion(0), end=circle.point_from_proportion(0.5), color=RED)
        dividing_line2 = Line(start=circle.point_from_proportion(0.75), end=circle.point_from_proportion(0.25), color=RED)

        self.play(Create(circle))
        self.wait(1)
        self.play(Create(dividing_line1))
        self.play(Create(dividing_line2))
        self.wait(1)

      #manim -pql LosCircle.py CircleDivision
        
    
class PointsOnCircle(Scene):
    def construct(self):
        circle = Circle(radius=3.0, color=GREEN)
        # Number of points required
        num_points = 16
        # Calculate each angle
        angles = [n * (360 / num_points) for n in range(num_points)]
        # Points on circumference of circle
        points = [circle.point_at_angle(n*DEGREES) for n in angles]
        # Create circles at each point
        circles = [Circle(radius=0.05, color=RED, fill_opacity=1).move_to(p) for p in points]
        # Add the circle to the scene
        self.add(circle)
        # Add each of the points to the scene
        for c in circles:
            self.add(c)    