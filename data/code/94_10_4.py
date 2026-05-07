if __name__ == '__main__':
    boolean_list_one = [False, False, False]
    boolean_list_two = [False, True, False]
    boolean_list_empty = []
    def check_at_least_one_true(bool_list):
        return any(bool_list)
    result_one = check_at_least_one_true(boolean_list_one)
    result_two = check_at_least_one_true(boolean_list_two)
    result_empty = check_at_least_one_true(boolean_list_empty)
    print(f"List one: {boolean_list_one}, At least one True: {result_one}")
    print(f"List two: {boolean_list_two}, At least one True: {result_two}")
    print(f"Empty list: {boolean_list_empty}, At least one True: {result_empty}")