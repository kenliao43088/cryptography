# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <openssl/dh.h>
"""

TYPES = """
typedef ... DH;
"""

FUNCTIONS = """
DH *DH_new(void);
void DH_free(DH *);
int DH_size(const DH *);
int DH_check(const DH *, int *);
int DH_check_pub_key(const DH *, const BIGNUM *, int *);
int DH_generate_key(DH *);
int DH_compute_key(unsigned char *, const BIGNUM *, DH *);
int DH_set_ex_data(DH *, int, void *);
void *DH_get_ex_data(DH *, int);
DH *d2i_DHparams(DH **, const unsigned char **, long);
int i2d_DHparams(const DH *, unsigned char **);
int DHparams_print_fp(FILE *, const DH *);
int DHparams_print(BIO *, const DH *);
"""

MACROS = """
int DH_generate_parameters_ex(DH *, int, int, BN_GENCB *);
"""

CUSTOMIZATIONS = """
"""
