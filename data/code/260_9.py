import math
def compare_list_means(list1, list2):
    mean1 = sum(list1) / len(list1) if list1 else 0
    mean2 = sum(list2) / len(list2) if list2 else 0
    if mean1 > mean2:
        return f"List 1 has the higher average. Mean of List 1: {mean1}, Mean of List 2: {mean2}"
    elif mean2 > mean1:
        return f"List 2 has the higher average. Mean of List 1: {mean1}, Mean of List 2: {mean2}"
    else:
        return f"Both lists have the same average. Mean: {mean1}"
if __name__ == '__main__':
    list_a = [10.5, 12.3, 8.9, 15.0]
    list_b = [5.1, 6.7, 4.2, 7.8]
    result = compare_list_means(list_a, list_b)
    print(result)