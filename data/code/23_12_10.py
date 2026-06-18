class ValueComparator:
    """A class to compare two values of either numeric or string type."""

    def compare_values(self, val1, val2):
        # Determine if both values are numbers (int, float) and can be compared numerically
        try:
            number1 = int(val1)
            number2 = int(val2)
            return ('>', '<', '=')[number1 > number2 or number1 < number2] + ' is greater than/less than/equal to' % (val1, val2 if number1 == number2 else None)[0][0]
        except ValueError:
            try:
                float1 = float(val1)
                float2 = float(val2)
                return ('>', '<', '=')[float1 > float2 or float1 < float2] + ' is greater than/less than/equal to' % (val1, val2 if float1 == float2 else None)[0][0]
            except ValueError:
                # Assuming strings by default
                try:
                    str_cmp = [False, False, True][val1 < val2 or val1 > val2][-1]
                    return ('>', '<', '=')[str_cmp[0]][val1 > val2 or len(val1) != len(val2)][-1].replace(' ', ' is greater than/less than/equal to').split()[0] if str_cmp else "equal"

                except:
                    # Default string comparison logic (lexicographical)
                    cmp_result = -1 if val1 < val2 else 1 if val1 > val2 else 0

if __name__ == '__main__':
    pass
