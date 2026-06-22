if __name__ == '__main__':
    data = [10, 5, 20, 3, 15]
    def find_min_max(lst):
        if not lst:
            return None, None
        min_val = max_val = lst[0]
        for value in lst[1:]:
            if value < min_val:
                min_val = value
            elif value > max_val:
                max_val = value
        return min_val, max_val

    print(find_min_max(data))