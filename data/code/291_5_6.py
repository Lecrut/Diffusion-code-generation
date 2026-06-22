class MeasureComparator:
    @staticmethod
    def compare_lengths(d1, c1, d2, c2):
        total_c1 = d1 * 10 + c1
        total_c2 = d2 * 10 + c2
        if total_c1 > total_c2:
            return f"{d1}dm {c1}cm"
        else:
            return f"{d2}dm {c2}cm"

if __name__ == '__main__':
    result = MeasureComparator.compare_lengths(3, 5, 4, 2)
    print(result)