class LengthComparator:
    def _format_result(self, a, b, relation):
        return f"{a} {relation} {b}"

    def compare(self, length_a, length_b):
        if length_a > length_b:
            return self._format_result(length_a, length_b, "is longer than")
        if length_a < length_b:
            return self._format_result(length_a, length_b, "is shorter than")
        return self._format_result(length_a, length_b, "is equal to")

if __name__ == '__main__':
    cmp = LengthComparator()
    val_one = 25.7
    val_two = 12.3
    out_one = cmp.compare(val_one, val_two)
    print(out_one)
    out_two = cmp.compare(10.0, 10.0)
    print(out_two)
    out_three = cmp.compare(5, 20)
    print(out_three)