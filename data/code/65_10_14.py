def get_sublist(lst):
    return lst[2:5]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500, 600]
    print("Sample list:", sample_list)
    sublist = get_sublist(sample_list)
    print("Sublist from index 2 to 4 (not inclusive):", sublist)