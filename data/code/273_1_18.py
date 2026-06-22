class Repeater:
    MAX_REPETITIONS = 10

    @staticmethod
    def repeat_action(action, N):
        if not isinstance(N, int) or N <= 0:
            raise ValueError("N must be a positive integer")
        
        result = []
        i = 0
        while i < N and len(result) < Repeater.MAX_REPETITIONS:
            result.append(action())
            i += 1
        
        return result

if __name__ == '__main__':
    def sample_action():
        return "Action"

    repeated_actions = Repeater.repeat_action(sample_action, 5)
    print(f"Repeated actions: {repeated_actions}")