#C represents the speed of light in meters per second and is approximately 300,000,000 meters per second
C= 300000000 

#asking for mass from the user and then multiplying it with C squared to get the equivalent Energy according to the law E=MC^2

def main():
    M=int(input("what's the Mass? "))
    print("ENERGY=",M*square(C))


#defining the square function 

def square(n):
    return n**2

#calling out the main function 

main ()
