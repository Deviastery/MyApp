a, b, c = [2.0, 10.0, 4.0]
ans = ans1 = ans2 = D = 1.0
if a == 0.0:
    ans = -(c / b)
    print(ans)
else:
    D = b ** 2.0 - 4.0 * a * c
    if D == 0:
        ans = -(b/(2*a))
        print(ans)
    elif D > 0:
        ans1 = (-b - D**(0.5)) / (2.0*a)
        ans2 = (-b + D**(0.5)) / (2.0*a)
        print(ans1, ans2)
    else:
        print('No answer')