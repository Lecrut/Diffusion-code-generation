class StringComparator:
    @staticmethod
    def later_string(s1: str, s2: str) -> str:
        if s1 > s2:
            return s1
        else:
            return s2

if __name__ == '__main__':
    comparator = StringComparator()
    print(comparator.later_string("apple", "banana"))