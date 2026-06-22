class Triangle:
    MINIMUM_SIDE_LENGTH = 1
    
    def __init__(self, side1, side2, side3):
        if not (side1 >= Triangle.MINIMUM_SIDE_LENGTH and 
                side2 >= Triangle.MINIMUM_SIDE_LENGTH and 
                side3 >= Triangle.MINIMUM_SIDE_LENGTH):
            raise ValueError("Side lengths must be at least {}".format(Triangle.MINIMUM_SIDE_LENGTH))
        
        self.sides = [side1, side2, side3]
    
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print("The perimeter of the triangle is:", triangle.perimeter())
    except ValueError as e:
        print(e)