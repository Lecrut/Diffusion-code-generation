if __name__ == '__main__':
    sample_sequence = ['Hello World']
    repetitions = 100
    repeated_list = '\n'.join([item for _ in range(repetitions) for item in sample_sequence])
    print(repeated_list)