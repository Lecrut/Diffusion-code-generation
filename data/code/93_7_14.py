if __name__ == '__main__':
    a = False
    b = False
    def are_both_false(x, y):
        if not isinstance(x, bool) or not isinstance(y, bool):
            raise ValueError("Both inputs must be boolean values.")
        return not x and not y
    print(are_both_false(a, b))