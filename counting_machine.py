class CountingMachine:
    def init(self, count):
        self.count = count

    def inc(self):
        self.count += 1

    def dec(self):
        self.count -= 1