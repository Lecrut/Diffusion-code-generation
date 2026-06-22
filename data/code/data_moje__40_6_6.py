class PrismCalculator:
    FACTOR = 2
    DEFAULT_LENGTH = 10.0
    DEFAULT_WIDTH = 5.0
    DEFAULT_HEIGHT = 7.0

    @staticmethod
    def _calculate_face_area(dim1, dim2):
        return dim1 * dim2

    def get_surface_area(self, length=None, width=None, height=None):
        l = self.DEFAULT_LENGTH if length is None else length
        w = self.DEFAULT_WIDTH if width is None else width
        h = self.DEFAULT_HEIGHT if height is None else height
        
        face_1 = self._calculate_face_area(l, w)
        face_2 = self._calculate_face_area(w, h)
        face_3 = self._calculate_face_area(h, l)
        
        total = face_1 + face_2 + face_3
        return self.FACTOR * total

if __name__ == '__main__':
    calculator = PrismCalculator()
    result = calculator.get_surface_area(5.0, 3.0, 4.0)
    print(result)