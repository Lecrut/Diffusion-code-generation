def concatenate_lists(list1, list2):
    return [item for sublist in (list1, list2) for item in sublist]

if __name__ == '__main__':
    sample_list1 = ["Hello", "World"]
    sample_list2 = ["Python", "Scripting"]
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)