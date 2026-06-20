class SystemStateChecker:
    STATE_A = 1
    STATE_B = 2
    STATE_C = 4
    STATE_D = 8

    @staticmethod
    def check_state(flag_a, flag_b, flag_c, flag_d):
        state = 0
        if flag_a:
            state |= SystemStateChecker.STATE_A
        if flag_b:
            state |= SystemStateChecker.STATE_B
        if flag_c:
            state |= SystemStateChecker.STATE_C
        if flag_d:
            state |= SystemStateChecker.STATE_D
        return state

if __name__ == '__main__':
    result = SystemStateChecker.check_state(True, False, True, True)
    print(result)