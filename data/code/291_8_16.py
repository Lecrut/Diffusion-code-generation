class LengthComparator:
    def compare(self, length1, unit1, length2, unit2):
        if unit1 == "fathom" and unit2 == "meter":
            length1 *= 6.0768
        elif unit1 == "meter" and unit2 == "fathom":
            length2 *= 6.0768
        if length1 > length2:
            return f"{length1} meters"
        elif length2 > length1:
            return f"{length2} {unit2}"
        else:
            return f"Equal: {length1} meters"

if __name__ == '__main__':
    comparator = LengthComparator()
    result1 = comparator.compare(3, "fathom", 18.2304, "meter")
    print(result1)
    result2 = comparator.compare(5, "meter", 3, "fathom")
    print(result2)