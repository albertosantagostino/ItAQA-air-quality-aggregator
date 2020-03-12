#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of Italy regions/provinces
"""

from enum import Enum, auto


class Region(Enum):
    """Enum holding Italy's regions"""
    # yapf: disable
    ABRUZZO             = auto()
    BASILICATA          = auto()
    CALABRIA            = auto()
    CAMPANIA            = auto()
    EMILIAROMAGNA       = auto()
    FRIULIVENEZIAGIULIA = auto()
    LAZIO               = auto()
    LIGURIA             = auto()
    LOMBARDIA           = auto()
    MARCHE              = auto()
    MOLISE              = auto()
    PIEMONTE            = auto()
    PUGLIA              = auto()
    SARDEGNA            = auto()
    SICILIA             = auto()
    TOSCANA             = auto()
    TRENTINOALTOADIGE   = auto()
    UMBRIA              = auto()
    VALLEDAOSTA         = auto()
    VENETO              = auto()
    UNSET               = auto()
    # yapf: enable

class Province(Enum):
    """Enum holding Italy's provinces"""
    # TODO: Understand if needed for future queries or if it's not relevant
    # yapf: disable
    AGRIGENTO           = auto()
    ALESSANDRIA         = auto()
    ANCONA              = auto()
    AOSTA               = auto()
    AREZZO              = auto()
    ASCOLIPICENO        = auto()
    ASTI                = auto()
    AVELLINO            = auto()
    BARI                = auto()
    BARLETTAANDRIATRANI = auto()
    BELLUNO             = auto()
    BENEVENTO           = auto()
    BERGAMO             = auto()
    BIELLA              = auto()
    BOLOGNA             = auto()
    BOLZANO             = auto()
    BRESCIA             = auto()
    BRINDISI            = auto()
    CAGLIARI            = auto()
    CALTANISSETTA       = auto()
    CAMPOBASSO          = auto()
    CARBONIAIGLESIAS    = auto()
    CASERTA             = auto()
    CATANIA             = auto()
    CATANZARO           = auto()
    CHIETI              = auto()
    COMO                = auto()
    COSENZA             = auto()
    CREMONA             = auto()
    CROTONE             = auto()
    CUNEO               = auto()
    ENNA                = auto()
    FERMO               = auto()
    FERRARA             = auto()
    FIRENZE             = auto()
    FOGGIA              = auto()
    FORLICESENA         = auto()
    FROSINONE           = auto()
    GENOVA              = auto()
    GORIZIA             = auto()
    GROSSETO            = auto()
    IMPERIA             = auto()
    ISERNIA             = auto()
    LASPEZIA            = auto()
    LAQUILA             = auto()
    LATINA              = auto()
    LECCE               = auto()
    LECCO               = auto()
    LIVORNO             = auto()
    LODI                = auto()
    LUCCA               = auto()
    MACERATA            = auto()
    MANTOVA             = auto()
    MASSACARRARA        = auto()
    MATERA              = auto()
    MESSINA             = auto()
    MILANO              = auto()
    MODENA              = auto()
    MONZAEDELLABRIANZA  = auto()
    NAPOLI              = auto()
    NOVARA              = auto()
    NUORO               = auto()
    OLBIATEMPIO         = auto()
    ORISTANO            = auto()
    PADOVA              = auto()
    PALERMO             = auto()
    PARMA               = auto()
    PAVIA               = auto()
    PERUGIA             = auto()
    PESAROEURBINO       = auto()
    PESCARA             = auto()
    PIACENZA            = auto()
    PISA                = auto()
    PISTOIA             = auto()
    PORDENONE           = auto()
    POTENZA             = auto()
    PRATO               = auto()
    RAGUSA              = auto()
    RAVENNA             = auto()
    REGGIOCALABRIA      = auto()
    REGGIOEMILIA        = auto()
    RIETI               = auto()
    RIMINI              = auto()
    ROMA                = auto()
    ROVIGO              = auto()
    SALERNO             = auto()
    MEDIOCAMPIDANO      = auto()
    SASSARI             = auto()
    SAVONA              = auto()
    SIENA               = auto()
    SIRACUSA            = auto()
    SONDRIO             = auto()
    TARANTO             = auto()
    TERAMO              = auto()
    TERNI               = auto()
    TORINO              = auto()
    OGLIASTRA           = auto()
    TRAPANI             = auto()
    TRENTO              = auto()
    TREVISO             = auto()
    TRIESTE             = auto()
    UDINE               = auto()
    VARESE              = auto()
    VENEZIA             = auto()
    VERBANOCUSIOOSSOLA  = auto()
    VERCELLI            = auto()
    VERONA              = auto()
    VIBOVALENTIA        = auto()
    VICENZA             = auto()
    VITERBO             = auto()
    UNSET               = auto()
    # yapf: disable
