import numpy as np

def validate_input(sequence, repetitions):
    if not isinstance(sequence, (list, tuple, np.ndarray)):
        raise ValueError("Sequence must be a list, tuple, or numpy array")
    if not isinstance(repetitions, int) or repetitions < 1:
        raise ValueError("Repetitions must be a positive integer")

def repeat_sequence_numpy(sequence, repetitions):
    validate_input(sequence, repetitions)
    return np.tile(np.array(sequence), (repetitions, 1))

if __name__ == '__main__':
    sequence_to_repeat = [0.1, 0.2, 0.3]
    number_of_repetitions = 3
    final_result = repeat_sequence_numpy(sequence_to_repeat, number_of_repetitions)
    print(final_result)