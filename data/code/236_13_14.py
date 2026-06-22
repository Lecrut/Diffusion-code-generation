import numpy as np

class ArrayReplicator:
    @staticmethod
    def replicate_row_vector(vector, repetitions):
        return np.tile(vector, (repetitions, 1))

if __name__ == '__main__':
    sample_vector = np.array([[1, 2, 3]])
    num_repetitions = 4
    replicated_array = ArrayReplicator.replicate_row_vector(sample_vector, num_repetitions)
    print(replicated_array)