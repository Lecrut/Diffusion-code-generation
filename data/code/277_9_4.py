def count_items(t):
    count = 0
    for _ in t:
        count += 1
    return count

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    print(count_items(sample_tuple))