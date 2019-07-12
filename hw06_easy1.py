import math
 
 
 
class Triangle:
    def __init__(self, A, B, C):
# Функция вычисляет длину стороны
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)
 
        self.A = A
        self.B = B
        self.C = C
#вычисляем длину стороны AB
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CA = sideLen(self.C, self.A)
 
# Вычисление площади треугольника по формуле Герона
    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2
 
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))
 
#Периметр треугольника
    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA
 
#Высоту треугольника
    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)
 
 
existing_triangle = Triangle((3, 2), (6, 7), (0, 12))
 
print(existing_triangle.areaTriangle())
print(existing_triangle.heightTriangle())
print(existing_triangle.perimeterTriangle())