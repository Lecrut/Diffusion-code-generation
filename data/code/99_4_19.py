def parse_and_compute(expression):
    def helper(s):
        if not s.isdigit() and '(' not in s:
            return int(s), 0

        i = s.find('(')
        j = len(s) - 1 - s[::-1].find(')')
        
        if i != -1 and j != -1 and i < j:
            sub_expr = s[i+1:j]
            left, right = helper(sub_expr)
            num = int(s[:i])
            if num > 0:
                return helper(f"{num * left + right}")[0], 0
            else:
                return helper(f"({num * left + right})")[0], 0
        
        return int(s), 0

    result, _ = helper(expression)
    return result

if __name__ == '__main__':
    print(parse_and_compute("(1+2)*(3+(4*5))"))