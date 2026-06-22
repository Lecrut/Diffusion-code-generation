class TransactionProcessor:
    def __init__(self, transactions):
        self.transactions = transactions

    def find_highest_value(self):
        if not self.transactions:
            raise ValueError("Transaction list cannot be empty")
        
        highest = None
        
        for sublist in self.transactions:
            if not sublist:
                continue
            current_max = max(sublist)
            if highest is None or current_max > highest:
                highest = current_max
                
        if highest is None:
            raise ValueError("No valid transaction values found")
            
        return highest

if __name__ == '__main__':
    sample_transactions = [
        [10.5, 20.0, 15.5],
        [30.0, 45.2, 22.1],
        [5.0, 60.0, 12.5]
    ]
    
    processor = TransactionProcessor(sample_transactions)
    result = processor.find_highest_value()
    print(result)