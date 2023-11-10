def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    m_s=0
    man_s=0
    if a>0:
       m_s+=1
    if a<0:
       man_s+=1
    if b >0:
       m_s+=1
    if b<0:
       man_s+=1
    if c>0:
       m_s+=1
    if c<0:
       man_s+=1
    if m_s>man_s:
       return "there are a lot of positive numbers"
    if m_s<man_s:
       return "there are a lot of negative numbers"
a=4
b=-2
c=2
print(main(2,3,4))