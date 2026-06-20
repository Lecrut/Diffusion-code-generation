class StringComparator:
    @staticmethod
    def later_string(s1, s2):
        return max(s1, s2)

if __name__ == '__main__':
    result = StringComparator.later_string("apple", "banana")
    print(result)