from dataclasses import make_dataclass
from typing import Dict, List

NAMES: List[str] = [
    "V1",
    "K1",
    "V2",
    "K2",
    "V3",
    "K3",
    "V4",
    "K4",
    "V5",
    "K5",
    "V6",
    "K6",
    "V7",
    "K7",
    "V8",
    "K8",
    "V9",
    "K9",
    "V10",
    "K10",
    "V11",
    "K11",
    "V12",
    "K12",
    "V13",
    "K13",
    "V14",
    "K14",
    "V15",
    "K15",
    "V16",
    "K16",
    "V17",
    "K17",
    "V18",
    "K18",
    "V19",
    "K19",
    "V20",
    "K20",
    "V21",
    "K21",
    "V22",
    "K22",
    "V23",
    "K23",
    "V24",
    "K24",
    "V25",
    "K25",
    "V26",
    "K26",
    "V27",
    "K27",
    "V28",
    "K28",
    "V29",
    "K29",
    "V30",
    "K30",
    "V31",
    "K31",
    "V32",
    "K32",
    "V33",
    "K33",
    "V34",
    "K34",
    "V35",
    "K35",
    "V36",
    "K36",
    "V37",
    "K37",
    "V38",
    "K38",
    "V39",
    "K39",
    "V40",
    "K40",
    "V41",
    "K41",
    "V42",
    "K42",
    "V43",
    "K43",
    "V44",
    "K44",
    "V45",
    "K45",
    "V46",
    "K46",
    "V47",
    "K47",
    "V48",
    "K48",
    "V49",
    "K49",
    "V50",
    "K50",
    "V51",
    "K51",
    "V52",
    "K52",
    "V53",
    "K53",
    "V54",
    "K54",
    "V55",
    "K55",
    "V56",
    "K56",
    "V57",
    "K57",
    "V58",
    "K58",
    "V59",
    "K59",
    "V60",
    "K60",
    "V61",
    "K61",
    "V62",
    "K62",
    "V63",
    "K63",
    "V64",
    "K64",
    "V65",
    "K65",
    "V66",
    "K66",
    "V67",
    "K67",
    "V68",
    "K68",
    "V69",
    "K69",
    "V70",
    "K70",
    "V71",
    "K71",
    "V72",
    "K72",
    "V73",
    "K73",
    "V74",
    "K74",
    "V75",
    "K75",
    "V76",
    "K76",
    "V77",
    "K77",
    "V78",
    "K78",
    "V79",
    "K79",
    "V80",
    "K80",
    "V81",
    "K81",
    "V82",
    "K82",
    "V83",
    "K83",
    "V84",
    "K84",
    "V85",
    "K85",
    "V86",
    "K86",
    "V87",
    "K87",
    "V88",
    "K88",
    "V89",
    "K89",
    "V90",
    "K90",
    "V91",
    "K91",
    "V92",
    "K92",
    "V93",
    "K93",
    "V94",
    "K94",
    "V95",
    "K95",
    "V96",
    "K96",
    "V97",
    "K97",
    "V98",
    "K98",
    "V99",
    "K99",
    "V100",
    "K100",
    "V101",
    "K101",
    "V102",
    "K102",
    "V103",
    "K103",
    "V104",
    "K104",
    "V105",
    "K105",
    "V106",
    "K106",
    "V107",
    "K107",
    "V108",
    "K108",
    "V109",
    "K109",
    "V110",
    "K110",
    "V111",
    "K111",
    "kf112",
    "kf113",
    "kf114",
    "kf115",
]

NUM: int = len(NAMES)

Parameters = make_dataclass(
    cls_name="Parameters",
    fields=[(name, int) for name in NAMES],
    namespace={"NAMES": NAMES, "NUM": NUM},
    frozen=True,
)

name2idx: Dict[str, int] = {k: v for v, k in enumerate(NAMES)}

C = Parameters(**name2idx)

del name2idx