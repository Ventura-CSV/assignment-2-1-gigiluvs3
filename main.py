def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc, f_perc, nb_perc for your results
    ##################################################
    """
    males = int (input ('Input a male value '))
    females = int (input ('Input a female value '))
    nb  = int (input ('Input a nb value '))
    total = males + females + nb 
    m_perc = males/total*100
    f_perc = females/total*100
    nb_perc = nb/total*100
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    print ('Total number of students:',total)
    print(
        f'The number of males, females and non-binary \t {males} \t {females} \t {nb}')
    print(
        f'The percentage of males, females and non-binary \t {m_perc: .2f}% \t {f_perc: .2f}% \t {nb_perc: .2f}%')
    return m_perc, f_perc, nb_perc


if __name__ == '__main__':
    main()
