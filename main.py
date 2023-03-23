import math

class Circle:
    def __init__(self, r):
        self.radius = r
    def calculate_diameter(self, r):
        return r * 2
    def calculate_circumference(self, r):
        return 2 * math.pi * r
    def calculate_area(self, r):
        return math.pi * r * r
    def grow(self, r):
        return r + 1
    def get_radius(self, r):
        return r

# Didn't have time to figure this out
# while True:
#     rad = float(input("Enter a radius in this format (x.xx): "))
#     try:
#         break
#     except ValueError as ve:
#         print('Incorrect answer')

print("Welcome to the the Circle Tester")
rad = float(input("Enter a radius in this format (x.xx): "))

while True:
    c1 = Circle(rad)
    print(f'Diameter : {c1.calculate_diameter(rad)}')
    print(f'Circumference: {c1.calculate_circumference(rad)}')
    print(f'Area: {c1.calculate_area(rad)}')
    grow = input('Would you like your circle to grow? (y/n) ')
    if grow.lower() == 'y':
        print('Stand by while your circle magically grows...')
        x = c1.grow(rad)
        rad = x
        continue
    else:
        print('Goodbye')
        break






