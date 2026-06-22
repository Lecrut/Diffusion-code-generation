def check_existence(data_list):
    if not data_list:
        return False
    found_active = False
    index = 0
    while index < len(data_list):
        if data_list[index]:
            found_active = True
            break
        index += 1
    return found_active

if __name__ == '__main__':
    samples = [
        [True, True],
        [False, False, False],
        [False, True, False, False],
        [],
        [False]
    ]
    results = [check_existence(sample) for sample in samples]
    for i, res in enumerate(results):
        print(f"sample {i}: {res}")