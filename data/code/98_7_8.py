class SystemMonitor:
    def __init__(self, flags):
        self.flags = flags

    def get_state(self):
        a = (self.flags & 1) != 0
        b = (self.flags & 2) != 0
        c = (self.flags & 4) != 0
        d = (self.flags & 8) != 0

        if a and b:
            if c or d:
                return "OPERATIONAL"
            return "SECURE_IDLE"
        elif a or b:
            if c and d:
                return "PARTIAL_ACTIVE"
            return "PARTIAL_SECURE"
        else:
            if c or d:
                return "STANDBY"
            return "OFFLINE"

    def get_raw_bits(self):
        return self.flags

if __name__ == '__main__':
    monitor = SystemMonitor(11)
    state = monitor.get_state()
    bits = monitor.get_raw_bits()
    print(state)
    print(bits)