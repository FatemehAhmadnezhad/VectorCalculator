from math import *


class Vec_3(object):
    def __init__(self, lenght, height, width):
        self._x = lenght
        self._y = height
        self._z = width

    def __str__(self):
        return f'[{self._x}; {self._y}; {self._z}]'

    def __add__(self, other):
        sum_x = self._x + other._x
        sum_y = self._y + other._y
        sum_x = self._z + other._z
        return Vec_3(sum_x, sum_y, sum_z)

    def __sub__(self, other):
        sum_x = self._x - other._x
        sum_y = self._y - other._y
        sum_z = self._z - other._z
        return Vec_3(sum_x, sum_y, sum_z)

    def __mul__(self, other):
        return (self._x * other._x)+(self._y * other._y)+(self._z * other._z)

    def __eq__(self, other):
        return (self._x == other._x) and (self._y == other._y) and (self._z == other._z)

    def __ne__(self, other):
        return (self._x != other._x) or (self._y != other._y) or (self._z != other._z)

    def __abs__(self):
        abs_vec = ((self._x**2)+(self._y**2)+(self._z**2))**0.5
        return abs_vec

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def unit(self):
        if self._x == 0 and self._y == 0 and self._z == 0:
            print('The input vector is the zero vector!!')
            return Vec_3(0, 0, 0)
        else:
            x1 = self._x/abs(self)
            y1 = self._y/abs(self)
            z1 = self._z/abs(self)
            return Vec_3(x1, y1, z1)

    def out_prod(self, other):
        cx = self._y*other._z-self._z*other._y
        cy = self._z*other._x-self._x*other._z
        cz = self._x*other._y-self._y*other._x
        return Vec_3(cx, cy, cz)

    def dist(self, other):
        distance = ((self._x - other._x)**2+(self._y - other._y)
                    ** 2+(self._z - other._z)**2)**0.2
        return distance

    def angle(self, other):
        costeta=self.__mul__(other)/(abs(self)*abs(other))
        if costeta>1 or costeta<-1:
            costeta=round(costeta)
        teta = acos(costeta)
        return teta
    def proj(self, other):
        px=(self.__mul__(other)/abs(other))*other._x
        py=(self.__mul__(other)/abs(other))*other._y
        pz=(self.__mul__(other)/abs(other))*other._z
        return Vec_3(px, py, pz)
    def rej(self, other):
        rx=self._x - 2*(self._x - other._x)
        ry=self._y - 2*(self._y - other._y)
        rz=self._z - 2*(self._z - other._z)
        return Vec_3(rx, ry, rz)
    def parall(self, other):
        return self.out_prod(other)==Vec_3(0, 0, 0)
    def prepend(self, other):
        return self.__mul__(other)==0
    def triangle_area(self, other):
        return abs(self.out_prod(other))*0.5
    def parallelogram_area(self, other):
        return abs(self.out_prod(other))
    def parallelepiped_vol(self,other1,other2):
        v=self.__mul__(other1.out_prod(other2))
        if v>0:
            return v
        elif v<0:
            return -v 
        else:
            return 'With these three vectors, a parallelogram is not made'
    def prism_vol(self,other1,other2):
        v2=self.__mul__(other1.out_prod(other2))
        if v>0:
            return v*0.5
        elif v<0:
            return -v*0.5
        else:
            return 'With these three vectors, a prism is not made'
    def pyramid_vol(self,other1,other2):
        v3=self.__mul__(other1.out_prod(other2))
        if v>0:
            return v/3
        elif v<0:
            return -v /3
        else:
            return 'With these three vectors, a pyramid is not made'

class Vec_2(Vec_3):
    def __init__(self, lenght, height, width,theta):
        Vec_3.__init__(self,lenght, height, width)
        self._theta=theta
    def rotate(self):
        xr=self._x*cos(self._theta)-self._y*sin(self._theta)
        yr=self._x*sin(self._theta)+self._y*cos(self._theta)
        return Vec_3(xr, yr, self._z)


