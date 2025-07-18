class Solution:
    def isPalindrome( n):
        s = str(abs(n))
        reversed_int = int(s[::-1]) 
        if reversed_int==n:
            return True
        else:
            return False    
    n=int(input("enter the number")) 
    p=isPalindrome(n)      
    print(p)