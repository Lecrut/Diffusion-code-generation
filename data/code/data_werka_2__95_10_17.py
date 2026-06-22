class Validator:
    POSITIVE_THRESHOLD = 0
    EVEN_CHECK = 2
    MAX_MITIGUE = 100

    def __init__(self, a, b, c):
        self.inputs = (a, b, c)

    def _check_value(self, val):
        messages = []
        if val <= self.POSITIVE_THRESHOLD:
            messages.append("not positive")
        elif val % self.EVEN_CHECK != 0:
            messages.append("odd")
        elif val >= self.MAX_MITIGUE:
            messages.append("too large")
        else:
            messages.append("valid")
        return messages

    def combine_and_report(self):
        a, b, c = self.inputs
        status_a = self._check_value(a)
        status_b = self._check_value(b)
        status_c = self._check_value(c)
        return {
            "inputs": self.inputs,
            "status_a": status_a[0],
            "status_b": status_b[0],
            "status_c": status_c[0]
        }

if __name__ == '__main__':
    v1 = Validator(10, 20, 30)
    print(v1.combine_and_report())
    v2 = Validator(-5, 101, 7)
    print(v2.combine_and_report())