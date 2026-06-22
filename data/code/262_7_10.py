def find_min_max(data):
    if not data:
        return (None, None)

    def helper(sublist):
        if not sublist:
            return (float('inf'), float('-inf'))
        min_val = max_val = sublist[0]
        for item in sublist:
            if isinstance(item, list):
                sub_min, sub_max = helper(item)
                if sub_min < min_val:
                    min_val = sub_min
                if sub_max > max_val:
                    max_val = sub_max
            else:
                if item < min_val:
                    min_val = item
                if item > max_val:
                    max_val = item
        return (min_val, max_val)
    return helper(data)
if __name__ == '__main__':
    sample_data = [3, [1, 4], 5, [2, [8, 9]], 0]
    print(find_min_max(sample_data))