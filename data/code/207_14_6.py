def max_element(lst):
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

if __name__ == '__main__':
    sample_list = [3.5, 2.1, 4.8, 1.9]
    print(max_element(sample_list))