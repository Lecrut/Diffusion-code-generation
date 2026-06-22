def verify_false_pair(left_state, right_state):
    left_is_false = left_state == False
    right_is_false = right_state == False
    return left_is_false and right_is_false

if __name__ == '__main__':
    first_flag = False
    second_flag = True
    evaluation = verify_false_pair(first_flag, second_flag)
    print(evaluation)