def symmetric_difference(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both arguments must be sets.")
    return set1 ^ set2

if __name__ == '__main__':
    SET_A = {1, 2, 3, 4}
    SET_B = {3, 4, 5, 6}
    SET_C = {'a', 'b', 'c'}
    SET_D = {'b', 'c', 'd'}

    try:
        result_ab = symmetric_difference(SET_A, SET_B)
        print("Symmetric difference of SET_A and SET_B:", result_ab)

        result_cd = symmetric_difference(SET_C, SET_D)
        print("Symmetric difference of SET_C and SET_D:", result_cd)
    except ValueError as e:
        print(e)