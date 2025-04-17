print("Números primos del 0 al 50")

pri= 0

while(pri<=50):

    if pri > 1:

        n= 2

        primo=True

        while (n*n<=pri):

            if pri % n == 0:

                primo= False

            n+=1

        if primo:

            print(pri)
            
    pri+=1

