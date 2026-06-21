class NameProcessor:
    @staticmethod
    def process_names(names):
        return sorted(set(name.upper() for name in names), reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'bob', 'Charlie', 'alice', 'Bob']
    print(NameProcessor.process_names(sample_names))