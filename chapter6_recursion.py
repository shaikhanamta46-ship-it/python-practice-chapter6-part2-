#recursion arefunctions that call itself 

#wap to sum of first n natural number using recursion
def calc_sum(n):
    if n == 0:
        return 0
    return n + calc_sum(n-1)
print(calc_sum(5))


#waf of recursive function to print all the elements of a list
def print_list(lst, idx):
    if idx == len(lst):
        return
    print(lst[idx])
    print_list(lst, idx + 1)
fruits = ["apple","banana","grapes","orange"]
print_list(fruits, 0)

#write a function factorial of a number using recursion
def calc_fact(n):
    if n == 0 or n == 1:
        return 1
    return n * calc_fact(n-1)
print(calc_fact(6))

#fibonacci series using recursion
def fibaconni(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibaconni(n-1) + fibaconni(n-2)

print(fibaconni(10))

#write a program to check the prime number using recursion
def is_prime(n, divisor=2):
    if n <= 1:
     return False
    if divisor >= n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor +1)
print(is_prime(29))

