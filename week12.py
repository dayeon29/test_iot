counts = 0
number = int(input("Input number : "))

for i in range(1, number+1):  # 1부터 입력한 수까지 반복
    if number % i == 0:  # 입력한 수를 1부터 입력된 수까지 나누어 떨어지는지 조건문으로 체크
        counts = counts + 1  # 약수 발견 시 카운트 값 증가
    print(i, end=' ')

if counts == 2:
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number! (divisors : {counts})")