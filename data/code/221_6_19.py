class Sorter:
    @staticmethod
    def middle_value(a, b, c):
        return (a + b + c) - min(a, b, c) - max(a, b, c)

if __name__ == '__main__':
    x = 5
    y = 2
    z = 8
    sorted_values = (min(x, y, z), Sorter.middle_value(x, y, z), max(x, y, z))
    print(sorted_values)