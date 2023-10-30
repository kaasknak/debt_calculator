import math

def main():
    print("Geef het totale bedrag aan schuld op:")
    debt = float(input())
    print("Geef de rente op:")
    interest = float(input())
    print("Geef het betalende maandbedrag op:")
    payment = float(input())
    print("Geef de eenmalige extra aflossing op:")
    extra = float(input())
    debt = debt - extra
    enough(debt, interest, payment)
    debt_left = debt
    months = 0
    paid = 0
    while debt_left > 0:
        if debt_left < payment:
            paid = paid + debt_left*(1+interest/100)**(1/12)
            debt_left = 0
        else:
            debt_left = debt_left*(1+interest/100)**(1/12)-payment
            paid = paid + payment
        months =  months + 1
    years = months/12
    years_whole = math.floor(years)
    months_left = months - years_whole*12
    print("Schuld afbetaald na "+str(years_whole)+" jaren en "+str(months_left)+" maanden.")
    print("Totaal bedrag betaald: €"+ str(paid)+" + €"+str(extra)+" aan extra aflossing.\n\n")
    close()

def enough(d, i, p):
    increase = d*((1+i/100)**(1/12)-1)
    if increase > p:
        print("De toename door de rente is groter dan je aflossing.\nDeze schuld kan je niet zo aflossen.\nProbeer opnieuw met een lager bedrag of een hogere afbetaling.")
        close()
    else:
        return

def close():
    print("Berekening is klaar!\nDruk op ENTER om het programma af te sluiten...")
    input()
    exit()

if __name__ == "__main__":
    main()
