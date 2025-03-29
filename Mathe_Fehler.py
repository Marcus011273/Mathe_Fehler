import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titel der App
st.title('Fehlerdiagnose & Lernstanderhebung (Mittelschule) – Quiz-Modus')

# Einführung
st.markdown('''
Diese App hilft Ihnen als Referendar:in dabei, häufige Schülerfehler im Mathematikunterricht zu erkennen, zu analysieren und gezielte Fördermaßnahmen zu entwickeln.

### Zielsetzungen:
- Förderung diagnostischer Kompetenzen
- Sensibilisierung für typische Fehlvorstellungen
- Planung didaktisch passender Reaktionen im Unterricht
''')

# Fehler 1: Bruchrechnung (Quiz)
st.header('1. Quiz: Fehlerdiagnose – Bruchrechnung')

st.markdown('''
**Schülerantwort (Wortgleichung):**
Zwei Drittel plus ein Viertel ergibt drei Siebtel.

**Was ist hier vermutlich passiert?**
''')

antwort1 = st.radio('Ihre Antwort:', [
    'Zähler und Nenner einfach addiert',
    'Zähler addiert, Nenner übernommen',
    'Brüche verwechselt mit Dezimalzahlen',
    'Rechenregel korrekt angewendet'
], key='bruch')

if st.button('Antwort überprüfen – Aufgabe 1'):
    if antwort1 == 'Zähler und Nenner einfach addiert':
        st.success('Richtig! Dieser typische Fehler entsteht, wenn Kinder die Rechenregel für Brüche nicht kennen.')
    else:
        st.error('Leider falsch. Richtig wäre: Zähler und Nenner einfach addiert.')

# Fehler 2: Dezimalrechnung (Quiz)
st.header('2. Quiz: Fehlerdiagnose – Dezimalzahlen')

st.markdown('''
**Schülerantwort (Wortgleichung):**
Eins Komma vier mal null Komma zwei ergibt achtundzwanzig.

**Was ist hier vermutlich passiert?**
''')

antwort2 = st.radio('Ihre Antwort:', [
    'Komma ignoriert, nur 14 × 2 gerechnet',
    'Falsches Umrechnen in Brüche',
    'Verwechslung mit Addition',
    'Richtig gerechnet'
], key='dezimal')

if st.button('Antwort überprüfen – Aufgabe 2'):
    if antwort2 == 'Komma ignoriert, nur 14 × 2 gerechnet':
        st.success('Richtig! Der Schüler hat das Komma ignoriert und nur mit den ganzen Zahlen gerechnet.')
    else:
        st.error('Leider falsch. Richtig wäre: Komma ignoriert, nur 14 × 2 gerechnet.')

# Fehler 3: Terme und Gleichungen (Quiz)
st.header('3. Quiz: Fehlerdiagnose – Gleichungslösen')

st.markdown('''
**Schülerantwort (Wortgleichung):**
x plus drei ist gleich fünf, also ist x gleich acht.

**Was ist hier vermutlich passiert?**
''')

antwort3 = st.radio('Ihre Antwort:', [
    'Addition falsch herum gedacht',
    'Unbewusst 5 + 3 gerechnet',
    'Ziel war x allein, aber falsche Umformung',
    'Korrekte Lösung'
], key='gleichung')

if st.button('Antwort überprüfen – Aufgabe 3'):
    if antwort3 == 'Unbewusst 5 + 3 gerechnet':
        st.success('Richtig! Der Schüler hat vermutlich die bekannte Rechnung 5 + 3 durchgeführt, statt umzuformen.')
    else:
        st.error('Leider falsch. Richtig wäre: Unbewusst 5 + 3 gerechnet.')

# Abschlussreflexion
st.header('Zusätzliche Reflexionsaufgabe für Referendar:innen')
st.markdown('''
- Entwickeln Sie eigene Fehlerbeispiele aus Ihrer Unterrichtspraxis.
- Welche Vorteile bietet es, Fehler systematisch zu analysieren?
- Planen Sie eine kurze Unterrichtssequenz, in der Sie gezielt auf einen häufigen Fehler eingehen und ihn aufarbeiten.
''')