def find_opposite_truth(is_truthy):
    true_state = is_truthy
    opposite_state = not true_state
    return opposite_state

if __name__ == '__main__':
    initial_value = True
    outcome = find_opposite_truth(initial_value)
    print(outcome)
    
    initial_value_two = False
    outcome_two = find_opposite_truth(initial_value_two)
    print(outcome_two)