def tally_items(sequence):
    count_dict = {}
    for item in sequence:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return dict(sorted(count_dict.items(), key=lambda x: x[1]))

if __name__ == '__main__':
    sample_list = [3, 1, 2, 3, 4, 2, 5, 1]
    print(f"Tally of items in {sample_list}: {tally_items(sample_list)}")