def compare_strings(str1, str2):
    len_diff = len(str1) - len(str2)
    if len_diff != 0:
        return ('longer', 'shorter') if len_diff > 0 else ('shorter', 'longer')
    alpha_diff = (str1 < str2, str1 > str2)
    if alpha_diff == (False, False):
        return ('equal', 'equal')
    return ('lesser', 'greater') if alpha_diff[0] else ('greater', 'lesser')
if __name__ == '__main__':
    print(compare_strings('apple', 'banana'))
    print(compare_strings('cat', 'bat'))
    print(compare_strings('dog', 'dog'))