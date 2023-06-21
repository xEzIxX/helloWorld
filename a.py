class Function:
    def value(self, x):
        raise NotImplementedError("이것은 함수값을 반환하는 추상메소드 입니다.")

class Quadratic(Function):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        f = self.a * x * x + self.b * x + self.c
        return str(f)

    def get_roots(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D > 0:
            x1 = (-self.b + D ** 0.5) / (2 * self.a)
            x2 = (-self.b - D ** 0.5) / (2 * self.a)
            return f"이 2차 방정식의 실근은 {x1}, {x2}입니다."
        elif D == 0:
            x = -self.b / (2 * self.a)
            return f"이 2차 방정식의 중근은 {x}입니다."
        else:
            return "이 2차 방정식은 허근을 가집니다."

F = Quadratic(1, -2, 1)
print("x가 5일 때 함수값:", F.value(5))
print(F.get_roots())