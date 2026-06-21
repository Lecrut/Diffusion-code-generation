class NumberList:
    SEED = [42, 88, 13, 7]
    
    @staticmethod
    def extract_initial(source):
        return source[0]

if __name__ == '__main__':
    sample_data = NumberList.SEED
    first_val = NumberList.extract_initial(sample_data)
    print(first_val)