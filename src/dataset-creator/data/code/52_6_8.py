def get_final_value(lst):
    return sum(1 for _ in lst) if isinstance(lst, list) else 0
if __name__ == '__main__':
    sample_list = [True] * 5 + [False] * 3
    print(get_final_value(sample_list))