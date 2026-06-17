def find_final_value(lst):
    return (lambda x: sum(x) if isinstance(x[0], list) else 1)(lst)[0] if lst and not all(isinstance(i, int) for i in lst) else sum(lst)
if __name__ == '__main__':
    data = [5, 3, 8, 2]
    final_explicit = 0
    for item in data:
        if isinstance(item, list):
            final_explicit += sum(item)
        else:
            final_explicit += item
    final_one_liner = sum([sum(sub_list) if isinstance(item, list) else item for item in data])
    print(f"Final value (Explicit): {final_explicit}")
    print(f"Final value (One-liner): {final_one_liner}")