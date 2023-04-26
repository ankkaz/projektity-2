from typing import Union


class Laskija:
    """Luokka, joka toteuttaa eri laskutoimituksia.

    Julkiset metodit:
        summaa(*args: Union[int, float]) -> Union[int, float]
        kerro(*args: Union[int, float]) -> Union[int, float]
    """

    def summaa(self, *args):
        """Palauttaa argumenttien summan.

        :param args: luvut, joiden summa lasketaan
        :type args: Union[int, float]
        :return: argumenttien summa
        :rtype: Union[int, float]
        """
        return sum(args)

    def kerro(self, *args):
        """Palauttaa argumenttien tulon.

        :param args: luvut, joiden tulo lasketaan
        :type args: Union[int, float]
        :return: argumenttien tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in args:
            tulo *= luku
        return tulo


class MonenLaskija(Laskija):
    """Luokka, joka toteuttaa eri laskutoimituksia, joissa voi olla kuinka monta lukua tahansa.

    Julkiset metodit:
        summaa(*args: Union[int, float]) -> Union[int, float]
        kerro(*args: Union[int, float]) -> Union[int, float]
    """

    pass


def argumenttien_tulostaja(**kwargs):
    """Tulostaa annetut avainsana-argumentit.

    :param kwargs: avainsana-argumentit
    """
    for avainsana, arvo in kwargs.items():
        print(f'Argumentin "{avainsana}" arvo on {arvo}.')
        

l = Laskija()
ml = MonenLaskija()

print(l.summaa(11, 31))
print(l.kerro(3, 12))
print()
print(ml.summaa(1, 2, 3, 4, 5))
print(ml.kerro(1, 2, 3, 4, 5))
print()
print(ml.summaa(1, 2, 3, 4, 5, 6, 7))
print(ml.kerro(1, 2, 3, 4, 5, 6 ,7))
print()
argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')
