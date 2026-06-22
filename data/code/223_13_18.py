def find_maximum(lst):
    if not lst:
        return None
    return max(lst)

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    print(f"Maximum of {sample_list}: {find_maximum(sample_list)}")