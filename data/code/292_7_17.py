class Ellipse:
    Ramanujan_A = 1 + (3 * 3.141592653589793 / (10 + (4 - 3 * 3.141592653589793) ** 0.5)) ** 0.5
    Ramanujan_B = 1 + (3 * 3.141592653589793 / (10 + (3 - 3 * 3.141592653589793) ** 0.5)) ** 0.5

    @staticmethod
    def calculate_perimeter(a, b):
        return 2 * (a + b) / 2 * (Ellipse.Ramanujan_A + Ellipse.Ramanujan_B)

if __name__ == '__main__':
    ellipse1 = Ellipse()
    perimeter1 = ellipse1.calculate_perimeter(3, 4)
    print(f"Perimeter for ellipse with semi-major axis 3 and semi-minor axis 4: {perimeter1}")

    ellipse2 = Ellipse()
    perimeter2 = ellipse2.calculate_perimeter(5, 7)
    print(f"Perimeter for ellipse with semi-major axis 5 and semi-minor axis 7: {perimeter2}")