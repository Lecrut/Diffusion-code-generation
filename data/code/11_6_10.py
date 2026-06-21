class EmptyCollectionError(Exception):
    def __init__(self, details):
        self.details = details
        super().__init__(details)

def determine_tail(source):
    if len(source) == 0:
        raise EmptyCollectionError("Source sequence contains no elements")
    return source[-1]

if __name__ == '__main__':
    valid_values = [10, 25, 42, 99, 7]
    final_value = determine_tail(valid_values)
    print(final_value)
    missing_values = []
    try:
        determine_tail(missing_values)
    except EmptyCollectionError as error:
        print(error.details)