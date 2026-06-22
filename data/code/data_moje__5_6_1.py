NEGATIVE_LENGTH_MSG = "Length cannot be negative"

class ImpossibleLengthError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.msg_value = msg

class LengthHolder:
    def __init__(self, first_len, second_len):
        self.first_len = first_len
        self.second_len = second_len

    def validate_and_compare(self):
        if self.first_len < 0:
            raise ImpossibleLengthError(NEGATIVE_LENGTH_MSG)
        if self.second_len < 0:
            raise ImpossibleLengthError(NEGATIVE_LENGTH_MSG)
        diff = abs(self.first_len - self.second_len)
        return diff

def run_comparison(a_val, b_val):
    holder = LengthHolder(a_val, b_val)
    return holder.validate_and_compare()

if __name__ == '__main__':
    try:
        result = run_comparison(10, 5)
        print(result)
    except ImpossibleLengthError as e:
        print(e.msg_value)