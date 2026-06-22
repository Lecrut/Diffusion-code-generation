MAX_DEPTH = 10

def count_items(nested_list):
    count = 0
    depth = 0
    stack = [(nested_list, depth)]

    while stack:
        current, current_depth = stack.pop()
        if isinstance(current, list) and current_depth < MAX_DEPTH:
            for item in current:
                stack.append((item, current_depth + 1))
        else:
            count += 1

    return count

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(count_items(sample_list))