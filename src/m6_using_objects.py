"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Melina Ferner.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()

    center_point1 = rg.Point(100, 100)
    radius1 = 50
    circle1 = rg.Circle(center_point1, radius1)
    circle1.attach_to(window)
    center_point2 = rg.Point(300, 100)
    radius2 = 30
    circle2 = rg.Circle(center_point2, radius2)
    circle2.fill_color = 'purple'
    circle2.attach_to(window)

    window.render()

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow()

    center_point = rg.Point(100, 100)
    radius = 70
    circle = rg.Circle(center_point, radius)
    circle.fill_color = "blue"
    circle.attach_to(window)
    print('**Circle**')
    print('Outline Thickness:', circle.outline_thickness)
    print('Fill Color:', circle.fill_color)
    print('Center:', circle.center)
    print('Center X-Coor:', circle.center.x)
    print('Center Y-Coor:', circle.center.y)

    corner1 = rg.Point(200, 50)
    corner2 = rg.Point(375, 150)
    rectangle = rg.Rectangle(corner1, corner2)
    rectangle.attach_to(window)

    print('**Rectangle**')
    print('Outline Thickness:', rectangle.outline_thickness)
    print('Fill Color:', rectangle.fill_color)
    rcenter = rectangle.get_center()
    print('Center:', rcenter)
    print('Center X-Coor:', rcenter.x)
    print('Center Y-Coor:', rcenter.y)

    window.render()

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()

    point1a = rg.Point(50, 100)
    point1b = rg.Point(350, 100)
    line1 = rg.Line(point1a, point1b)
    line1.attach_to(window)
    point2a = rg.Point(50, 200)
    point2b = rg.Point(350, 200)
    line2 = rg.Line(point2a, point2b)
    line2.thickness = 5
    line2.attach_to(window)
    midpoint = line2.get_midpoint()
    print('Midpoint:', midpoint)
    print('Midpoint X-Coor:', midpoint.x)
    print('Midpoint Y-Coor:', midpoint.y)

    window.render()
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
