class Consumer:
    def __init__(self, w):
        self.wealth = w
    
    def earn(self, y):
        self.wealth += y
    
    def spend(self, x):
        new_wealth = self.wealth - x
        if new_wealth < 0:
            print("Insufficient funds")
        else:
            self.wealth = new_wealth
